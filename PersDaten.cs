using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CoronaAppMeVs1
{
    [Activity(Label = "PersDaten")]
    public class PersDaten : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            // Create your application here
            SetContentView(Resource.Layout.PersDaten);

            var btnWeiter = FindViewById<Button>(Resource.Id.btnPersWeiter);

            btnWeiter.Click += delegate
            {
                Intent nextActivity = new Intent(this, typeof(Symptome));
                StartActivity(nextActivity);
            };
        }
    }
}