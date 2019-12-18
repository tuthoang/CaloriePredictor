package com.ec601.predictor;

import androidx.annotation.NonNull;

import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class Calorie {
    private float calorie;
    private String date;
    private String foodtype;
    public Calorie(){
    }

    public Calorie(float calorie, String foodtype){
        this.calorie = calorie;
//        this.calorie = 500;
        this.foodtype = foodtype;
        Calendar calendar;
        calendar = Calendar.getInstance();
        Format formatter = new SimpleDateFormat("YYYY MM dd");
        String s = formatter.format(new Date());
//        String s = "2019 11 28";
        date = s;
    }
    public Calorie(float calorie, String foodtype, String date){
        this.calorie = calorie;
        this.foodtype = foodtype;
        this.date = date;
    }
    public String getCalorie() {return String.valueOf(calorie);}
    public String getDate() {return date;}
    public String getFoodtype(){return foodtype;}

    @NonNull
    @Override
    public String toString() {
        return String.valueOf(calorie);
    }
}
