// Fill out your copyright notice in the Description page of Project Settings.


#include "PIDControllerFunctionLibrary.h"

float UPIDControllerFunctionLibrary::PIDCalculation(float DeltaTime, float P, float I, float D, float Bias, 
	float CurrentValue, float DesiredValue, UPARAM(ref) float& Integral, UPARAM(ref) float& ErrorPrior)
{	
	float pError = CurrentValue - DesiredValue;
	float pDerivative = (pError - ErrorPrior) / DeltaTime;
	
	//if (GEngine)GEngine->AddOnScreenDebugMessage(-1, 0.0f, FColor::Yellow, 
	//			FString::Printf(TEXT("Time elapsed: %f seconds"), DeltaTime));
	
	// Set referenced Variables
	Integral += pError * DeltaTime;
	ErrorPrior = pError;

	return ((ErrorPrior * P) + (Integral * I) + (pDerivative * D) + Bias) * DeltaTime;
}


float UPIDControllerFunctionLibrary::PIDCalculationRotation(float DeltaTime, float P, float I, float D, float Bias, 
	float CurrentValue, float DesiredValue, UPARAM(ref) float& Integral, UPARAM(ref) float& ErrorPrior)
{
	float pError = DesiredValue - CurrentValue;

	// Unreal Engine Rotation Error correction
	if (pError > 180) {
		pError -= 360;
	} else if (-180 > pError) {
		pError += 360;
	};

	float pDerivative = (pError - ErrorPrior) / DeltaTime;

	//if (GEngine)GEngine->AddOnScreenDebugMessage(-1, 0.0f, FColor::Yellow, FString::Printf(TEXT("Time elapsed: %f seconds"), DeltaTime));

	// Set referenced Variables
	Integral += pError * DeltaTime;
	ErrorPrior = pError;

	return ((ErrorPrior * P) + (Integral * I) + (pDerivative * D) + Bias) * DeltaTime;
}