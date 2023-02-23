# predict-insurance-cost
This modle predicts insurance cost for insurance company based on given data such as- [Age, Sex, BMI, Childern, Smoker, Region-(in US), Charges in USD] about patients.
This is a linear model, therfore I wished to find a set of coefficients that best satisfies:
Charges in USD ≈ α0 + α1 · age + α2 · Sex + α3 · BMI + α4 · Childern + α5 · Smoker + α6 · Region.
To get that I used the least squares method, and some manipulation of the data.
After some manipulation the main goal was to fine the vector x = [α0, α1, α2...] that best satisfies:(for example)
Charges in USD ≈ α0 + α1 · Age + α2 · Male + α3 · Female + α4 · BMI 
+α5 · Childern + α6 · Smoker + α7 · Non-smoker
+α8 · Region1 + α8 · Region2 + α8 · Region3 + α8 · Region4

