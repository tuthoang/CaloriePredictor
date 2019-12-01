package com.example.predictor.ui.main;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.example.predictor.R;

/**
 * A placeholder fragment containing a simple view.
 */
public class PlaceholderFragment extends Fragment {

    private static final String ARG_SECTION_NUMBER = "section_number";
    private String TAG = "Place Holder Fragment";
    private PageViewModel pageViewModel;
    private FirebaseRecyclerAdapter<Calorie, CalorieViewHolder> adapter;
//    private int index;
    private static final String[] TAB_TITLES = new String[]{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    private String d;
    private String dayofyear;
    public static PlaceholderFragment newInstance(int index) {
//        this.index = index;
        Log.e("GASASA", String.valueOf(index));
        PlaceholderFragment fragment = new PlaceholderFragment();
        Bundle bundle = new Bundle();
        bundle.putInt(ARG_SECTION_NUMBER, index);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState != null)
            return;
//        pageViewModel = ViewModelProviders.of(this).get(PageViewModel.class);
        else {
            int index = 0;
            if (getArguments() != null) {
                index = getArguments().getInt(ARG_SECTION_NUMBER);
                Log.e(TAG, "ARGS NOT NULL   " + index);

            } else {
                Log.e(TAG, "ARGS ARE NULLL");
            }
            d = TAB_TITLES[index];

            Log.e(TAG, d);
            Log.e(TAG, "==========");
            Calendar calendar;
            calendar = Calendar.getInstance();
            Format formatter = new SimpleDateFormat("YYYY MM dd");
            Date today = new Date();
            String today_str = formatter.format(today);
            DateFormat format2=new SimpleDateFormat("EEEE");
            String dayAbbrev=format2.format(today);
            int ind = Arrays.asList(TAB_TITLES).indexOf(dayAbbrev);
            calendar.setTime(today);

            calendar.add(Calendar.DAY_OF_YEAR, -(ind-index));
            Date DayForName = calendar.getTime();

            dayofyear = formatter.format(DayForName);
            Log.e(TAG, today_str + "      " + dayofyear);
        }
//        pageViewModel.setIndex(index);

    }

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_calorie_log, container, false);
        RecyclerView recyclerView = root.findViewById(R.id.list);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
        String foodtype = "Sandwich";
        final Calorie c = new Calorie(240, foodtype);
        Toast.makeText(this.getActivity(), "View log", Toast.LENGTH_LONG);
        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        String myUserId = user.getUid();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference();
        Calendar calendar;
        calendar = Calendar.getInstance();
        Format formatter = new SimpleDateFormat("YYYY MM dd");
        Date today = new Date();
        String today_str = formatter.format(today);
        calendar.setTime(today);

        calendar.add(Calendar.DAY_OF_YEAR, -7);
        Date lastweek = calendar.getTime();
        String lastweek_str = formatter.format(lastweek);
//        Log.e(TAG, today_str + "      " + lastweek_str);
        Query myTopPostsQuery = myRef.child("users")
                                .child(myUserId)
                                .child("meals")
                                .orderByChild("date").equalTo(dayofyear);
        FirebaseRecyclerOptions<Calorie> options = new FirebaseRecyclerOptions.Builder<Calorie>()
                .setQuery(myTopPostsQuery, new SnapshotParser<Calorie>() {
                    @NonNull
                    @Override
                    public Calorie parseSnapshot(@NonNull DataSnapshot snapshot) {
                        Log.e(TAG, String.valueOf(snapshot.getValue()));
                        Map<String, Object> td = (HashMap<String,Object>) snapshot.getValue();
                        String date = (String)td.get("date");
                        String foodtype = (String)td.get("foodtype");
                        float calorie = Float.parseFloat((String)td.get("calorie"));
                        Calorie c = new Calorie(calorie, foodtype, date);

                        return c;
                    }
                })
                .build();

        adapter = new FirebaseRecyclerAdapter<Calorie, CalorieViewHolder>(options) {

            @Override
            protected void onBindViewHolder(@NonNull CalorieViewHolder calorieViewHolder, int position, @NonNull Calorie calorie) {
                Log.e(TAG, calorie.getCalorie());
                calorieViewHolder.setCalorieView(String.valueOf(calorie.getCalorie()), calorie.getFoodtype(), calorie.getDate());
            }

            @NonNull
            @Override
            public CalorieViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
                View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.sample_my_item, parent, false);
                return new CalorieViewHolder(view);
            }

        };
        recyclerView.setAdapter(adapter);
        return root;
    }

    @Override
    public void onStart() {
        super.onStart();
        adapter.startListening();
    }

    @Override
    public void onStop() {
        super.onStop();

        if (adapter != null) {
            adapter.stopListening();
        }
    }
}