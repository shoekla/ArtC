package com.example.abirshukla.artc;

/**
 * Created by abirshukla on 2/25/17.
 */
public class DataForUser {
    public static String user = "";
    public static String getUser() {
        return user;
    }
    public static int logOut = 0;
    public static int firstTime = 1;
    public static int errorCount = 0;

    public static void setUser(String s) {
        user = s;
    }
}