package me.maniknarang.homesafehome;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;

/**
 * Created by maniknarang on 3/25/18.
 */

public class SplashScreen extends AppCompatActivity {
    // Splash screen time in milli seconds (3 seconds currently)
    private static final int SPLASH_SCREEN_TIME = 3000;

    @SuppressLint("NewApi")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_screen);

        // Create a handler for the splash screen
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent splashScreen = new Intent(SplashScreen.this, MainActivity.class);
                startActivity(splashScreen);
                finish();
            }
        }, SPLASH_SCREEN_TIME);
    }
}
