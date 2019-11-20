package com.example.secondpic2;

import android.Manifest;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.FileProvider;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MainActivity extends AppCompatActivity {

    Button take;
    Button save;
    ImageView foodPic;
    String pathTofile;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if(Build.VERSION.SDK_INT >=23){
            requestPermissions(new String[]{Manifest.permission.CAMERA,Manifest.permission.WRITE_EXTERNAL_STORAGE},2);
        }
        take = findViewById(R.id.buttontake);
        save = findViewById(R.id.buttonsave);
        foodPic = findViewById(R.id.foodPic_imageView);
        take.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                takepicture();
            }
        });
        save.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                galleryAddPic();
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 1 && resultCode == RESULT_OK) {
            Bitmap bitmap = BitmapFactory.decodeFile(pathTofile);
            foodPic.setImageBitmap(bitmap);
        }
    }

    private void takepicture(){
        Intent takepic = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takepic.resolveActivity(getPackageManager()) != null){
            File photoFile = null;
            photoFile = createPhotoFile();
            if(photoFile !=null){
                pathTofile = photoFile.getAbsolutePath();
                Log.d("filepathprint",pathTofile);
                Uri photoURI = FileProvider.getUriForFile(MainActivity.this, "com.example.secondpic2", photoFile);
                takepic.putExtra(MediaStore.EXTRA_OUTPUT, photoURI);
                startActivityForResult(takepic, 1);
                //galleryAddPic();
            }
        }
    }

    private File createPhotoFile() {
        // Create an image file name
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        String imageFileName = "JPEG_" + timeStamp + "_";
        File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
        File image = null;
        try {
            image = File.createTempFile(
                    imageFileName,  /* prefix */
                    ".jpg",         /* suffix */
                    storageDir      /* directory */
            );
        } catch (IOException e) {
            Log.d("mylog", "Excep : " + e.toString());
        }
        return image;
    }

    private void galleryAddPic() {
        Log.d("galleryaddpicprint",pathTofile);
        Intent mediaScanIntent = new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE);
        File f = new File(pathTofile);
        Uri contentUri = Uri.fromFile(f);
        mediaScanIntent.setData(contentUri);
        this.sendBroadcast(mediaScanIntent);
    }
    private void showPhoto(Uri photoUri){
        Intent intent = new Intent();
        intent.setAction(Intent.ACTION_VIEW);
        intent.setDataAndType(photoUri, "image/*");
        startActivity(intent);
    }
}

