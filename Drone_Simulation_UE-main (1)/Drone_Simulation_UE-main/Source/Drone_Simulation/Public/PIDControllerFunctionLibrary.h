// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "PIDControllerFunctionLibrary.generated.h"


/**
 *
 */
UCLASS()
class DRONE_SIMULATION_API UPIDControllerFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
		UFUNCTION(BlueprintCallable, Category = "PID Controller")
		static float PIDCalculation(float DeltaTime, float P, float I, float D, float Bias, 
			float CurrentValue, float DesiredValue, UPARAM(ref) float& Integral, UPARAM(ref) float& ErrorPrior);
		
		UFUNCTION(BlueprintCallable, Category = "PID Controller")
		static float PIDCalculationRotation(float DeltaTime, float P, float I, float D, float Bias, 
			float CurrentValue, float DesiredValue, UPARAM(ref) float& Integral, UPARAM(ref) float& ErrorPrior);
};
