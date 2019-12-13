package com.ec601.predictor.ui.main;

import android.view.View;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.ec601.predictor.R;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class CalorieViewHolder extends RecyclerView.ViewHolder {
    private View view;

    CalorieViewHolder(View itemView){
        super(itemView);
        view = itemView;
    }

    void setCalorieView(String calorie, String food, String date){
        TextView calView = view.findViewById(R.id.calorie_count);
        calView.setText(calorie);
        TextView foodView = view.findViewById(R.id.foodtype);
        foodView.setText(food);
        TextView dateView = view.findViewById(R.id.date);
        SimpleDateFormat format1=new SimpleDateFormat("yyyy MM dd");
        Date dt1= null;
        try {
            dt1 = format1.parse(date);
        } catch (ParseException e) {
            e.printStackTrace();
        }
        DateFormat format2=new SimpleDateFormat("EEEE");
        String finalDay=format2.format(dt1);

        dateView.setText(date);
    }
}
