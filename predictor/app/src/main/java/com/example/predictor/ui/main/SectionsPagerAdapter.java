package com.example.predictor.ui.main;

import android.content.Context;
import android.util.Log;
import android.widget.TableLayout;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.example.predictor.R;

/**
 * A [FragmentPagerAdapter] that returns a fragment corresponding to
 * one of the sections/tabs/pages.
 */
public class SectionsPagerAdapter extends FragmentPagerAdapter {

    @StringRes
    private static final String[] TAB_TITLES = new String[]{"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    private final Context mContext;
    private FragmentManager fm;
    public SectionsPagerAdapter(Context context, FragmentManager fm) {
        super(fm);
        this.fm = fm;
        mContext = context;

    }

    @Override
    public Fragment getItem(int position) {
        // getItem is called to instantiate the fragment for the given page.
        // Return a PlaceholderFragment (defined as a static inner class below).
        return PlaceholderFragment.newInstance(position);
    }

    @Nullable
    @Override
    public CharSequence getPageTitle(int position) {
        return TAB_TITLES[position];
    }

    @Override
    public int getCount() {
        // Show 2 total pages.
        return 7;
    }
}