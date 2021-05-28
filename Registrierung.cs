using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;

namespace CoronaAppMeVs1
{
    [Activity(Label = "Registrierung")]
    public class Registrierung : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            // Create your application here
            SetContentView(Resource.Layout.Registrierung);

            var btnRegister = FindViewById<Button>(Resource.Id.btnRegister);

            btnRegister.Click += delegate
            {
                Intent nextActivity = new Intent(this, typeof(PersDaten));
                StartActivity(nextActivity);

                string http = "http://10.0.2.2:58867/helloDB?message=store";

                EditText myBenutzer = FindViewById<EditText>(Resource.Id.edtPseudonym);
                http += "&parameter1=" + myBenutzer.Text;
                EditText myBirthday = FindViewById<EditText>(Resource.Id.edtGeburtsdatum);
                http += "&parameter2=" + myBirthday.Text;
                RadioGroup myGeschlecht = FindViewById<RadioGroup>(Resource.Id.radioGroupGeschlecht);
                if (myGeschlecht.CheckedRadioButtonId == Resource.Id.rBtnMan)
                {
                    http += "&parameter3=Männlich";
                }
                else if (myGeschlecht.CheckedRadioButtonId == Resource.Id.rBtnWoman)
                {
                    http += "&parameter3=Weiblich";
                }
                else if (myGeschlecht.CheckedRadioButtonId == Resource.Id.rBtnDivers)
                {
                    http += "&parameter3=Divers";
                }

                EditText myPostleitzahl = FindViewById<EditText>(Resource.Id.edtPostleitzahl);
                http += "&parameter4=" + myPostleitzahl.Text;

                WebRequest request = WebRequest.Create(http);
                request.Method = "GET";
                WebResponse response = request.GetResponse();
            };
        }
    }
}