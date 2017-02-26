package com.example.abirshukla.artc;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

/**
 * Created by Pranav on 2/25/2017.
 */

public class SwipeActivity extends AppCompatActivity {
    ImageView artImage;
    TextView artName;
    TextView artIst;
    Button like;
    Button info;
    Button dislike;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_swipe);
    }

    public void swipe( View view ) {
        artImage = (ImageView) findViewById(R.id.artView);
        artName = (TextView) findViewById(R.id.artName);
        artIst = (TextView) findViewById(R.id.artIst);
        like = (Button) findViewById(R.id.Like);
        info = (Button) findViewById(R.id.Info);
        dislike = (Button) findViewById(R.id.Dislike);

    }
}
