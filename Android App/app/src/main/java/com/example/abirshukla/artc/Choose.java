package com.example.abirshukla.artc;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.InputStream;
import java.net.URL;

/**
 * Created by Pranav on 2/25/2017.
 */

public class Choose extends AppCompatActivity {
    ImageView artImage;
    TextView artName;
    TextView artIst;
    Button likeButton;
    Button infoButton;
    Button dislikeButton;
    ImageView imageView;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_swipe);
        imageView = (ImageView) findViewById(R.id.artView);
        String imgUrl = "http://en.most-famous-paintings.com/Art.nsf/O/8XYFFG/$File/Leonardo-Da-Vinci-Mona-Lisa.JPG";

        new DownLoadImageTask(imageView).execute(imgUrl);
    }

    public void swipe(View view) {
        artImage = (ImageView) findViewById(R.id.artView);
        artName = (TextView) findViewById(R.id.artName);
        artIst = (TextView) findViewById(R.id.artIst);
        likeButton = (Button) findViewById(R.id.Like);
        infoButton = (Button) findViewById(R.id.Info);
        dislikeButton = (Button) findViewById(R.id.Dislike);

        likeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        infoButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        dislikeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });
    }


    private class DownLoadImageTask extends AsyncTask<String, Void, Bitmap> {
        ImageView imageView;

        public DownLoadImageTask(ImageView imageView) {
            this.imageView = imageView;
        }

        /*
            doInBackground(Params... params)
                Override this method to perform a computation on a background thread.
         */
        protected Bitmap doInBackground(String... urls) {
            String urlOfImage = urls[0];
            Bitmap logo = null;
            try {
                InputStream is = new URL(urlOfImage).openStream();
                /*
                    decodeStream(InputStream is)
                        Decode an input stream into a bitmap.
                 */
                logo = BitmapFactory.decodeStream(is);
            } catch (Exception e) { // Catch the download exception
                e.printStackTrace();
            }
            return logo;
        }

        /*
            onPostExecute(Result result)
                Runs on the UI thread after doInBackground(Params...).
         */
        protected void onPostExecute(Bitmap result) {
            imageView.setImageBitmap(result);
        }
    }
}


