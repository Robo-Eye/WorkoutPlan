# WorkoutPlan

Contributers: Tyler Fontana, Aaron McFeaters, John Burke  
  
Project Goal:  
Our website creates workout regimen that is tailored to the users’ goals that they input. A personalized regimen will be created for the user based on information they enter, such as gender, age, weight, and their workout goals. The user will be able to save the created workout for future reference. When the user updates their workout, the saved workout will be replaced with the newly updated workout.  

Users can save their workouts by making an account. The account requires a unique username, unique email, and a password. The password is hashed before being stored and uses a pepper key for additional security.  

The user’s geolocation will be retrieved so our website can check dynamically to see whether the weather in their area is fit for outdoor based workouts, such as running. We use the national weather service’s weather API in order to find out the weather information.  

If the user doesn’t create an account, they will only have access to viewing workouts individually across the website based on what they are looking to train (Abs, Biceps, Chest, Cardio, etc.…) to reach a particular goal, however that goal may be more of a broad goal then a tailored one. The non-registered users will not be able to create or save personalized workout plans. Such features will be only available to users who have created an account.  
  
To run: run routes.py using a python Flask interpreter.  
