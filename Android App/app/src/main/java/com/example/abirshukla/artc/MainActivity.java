package com.example.abirshukla.artc;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;

public class MainActivity extends AppCompatActivity {


    SharedPreferences sharedPref;
    public boolean okay = true;
    public boolean checkFire = true;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void login(View view) {
        final EditText user = (EditText) findViewById(R.id.editText);
        final EditText pas = (EditText) findViewById(R.id.editText2);
        //final EditText pho = (EditText) findViewById(R.id.editText3);
        final String userName = user.getText().toString();
        final String password = pas.getText().toString();
        //final String phone = pho.getText().toString();
        final FirebaseDatabase database = FirebaseDatabase.getInstance();
        final DatabaseReference myRef = database.getReference();
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                if (checkFire) {
                    String users = (String) dataSnapshot.child("Users").getValue().toString();
                    //String phones = (String) dataSnapshot.child("phones").getValue().toString();
                    String passW = (String) dataSnapshot.child("PassW").getValue().toString();
                    //String test = (String) dataSnapshot.child("Movies").getValue().toString();
                    System.out.println("Info: users: " + users);
                    System.out.println("Info: passw: " + passW);

                    String[] arr = users.split(",");
                    String[] passArr = passW.split(",");
                    System.out.println("Info: arrLen: " + arr.length);

                    System.out.println("Info: pasLen: " + passArr.length);
                    for (int i = 0; i < arr.length; i++) {
                        //System.out.println("Info: "+arr[i]);
                        if (arr[i].equals(userName)) {
                            if (passArr[i].equals(password)) {
                                Intent h = new Intent(MainActivity.this, Choose.class);
                                DataForUser.setUser(userName);

                                h.putExtra("say","");
                                startActivity(h);

                                return;
                            }
                            Toast.makeText(getApplicationContext(), "User Name already in System",
                                    Toast.LENGTH_SHORT).show();
                            return;
                        }
                    }
                    DataForUser.setUser(userName);
                    String url = "http://abirshukla.pythonanywhere.com/artC/addUser/" + userName;
                    getHTML(url);
                    if (!okay) {
                        Toast.makeText(getApplicationContext(), "Error Occured Please try again later",
                                Toast.LENGTH_SHORT).show();
                        return;
                    }
                    users = users + "," + userName;
                    passW = passW + "," + password;
                    //phones = phones+","+phone;
                    checkFire = false;
                    myRef.child("PassW").setValue(passW);
                    myRef.child("Users").setValue(users);
                    //myRef.child("phones").setValue(phones);

                    Toast.makeText(getApplicationContext(), "Your In!",
                            Toast.LENGTH_SHORT).show();
                    Intent h = new Intent(MainActivity.this, Choose.class);
                    h.putExtra("say","");
                    startActivity(h);
                    return;

                }



            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }


        });

    }
    public void getHTML(final String url) {
        System.out.println("Begin HTML");
        System.out.println("Final Url: " + url);
        final String[] d = new String[1];
        Ion.with(getApplicationContext())
                .load(url)
                .asString()
                .setCallback(new FutureCallback<String>() {
                    @Override
                    public void onCompleted(Exception e, String result) {
                        System.out.println("First Result: " + result);
                        okay = result.contains("All Good!");
                    }
                });
    }
    @Override
    protected void onSaveInstanceState(Bundle savedInstanceState) {
        super.onSaveInstanceState(savedInstanceState);
        savedInstanceState.putString("user",DataForUser.getUser());
        super.onSaveInstanceState(savedInstanceState);

    }

    @Override
    protected void onDestroy() {
        SharedPreferences.Editor editor = sharedPref.edit();
        String user = DataForUser.getUser();
        editor.putString("user", user);
        editor.commit();
        super.onDestroy();
    }

    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);
        String email = savedInstanceState.getString("email");
    }
}
