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
    Button likeButton;
    Button infoButton;
    Button dislikeButton;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_swipe);
    }

    public void swipe( View view ) {
        artImage = (ImageView) findViewById(R.id.artView);
        artName = (TextView) findViewById(R.id.artName);
        artIst = (TextView) findViewById(R.id.artIst);
        likeButton = (Button) findViewById(R.id.Like);
        infoButton = (Button) findViewById(R.id.Info);
        dislikeButton = (Button) findViewById(R.id.Dislike);

        likeButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

            }
        });

        infoButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

            }
        });

        dislikeButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

            }
        });
    }
}
