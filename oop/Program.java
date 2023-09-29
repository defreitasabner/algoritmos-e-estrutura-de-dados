package oop;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        Thermometer thermometer = new Thermometer();
        boolean isRunning = true;

        while (isRunning) {
            System.out.println("Para qual escala deseja converter (c/f)?");
            String scaleInput = scanner.nextLine();
            
            if(scaleInput.equals("c") || scaleInput.equals("C")) {
                System.out.println("Você selecionou converter F° -> C°");
            }
            else if (scaleInput.equals("f") || scaleInput.equals("F")) {
                System.out.println("Você selecionou converter C° -> F°");
            }
            else {
                break;
            }

            System.out.println("Digite a temperatura que deseja converter:");
            
            double inputTemperature = Double.parseDouble(scanner.nextLine());

            double outputTemperature;
            String outpuString;
            if(scaleInput.equals("c") || scaleInput.equals("C")) {
                outputTemperature = thermometer.convertFahrenheitToCelsius(inputTemperature);
                outpuString = "A temperatura %.1f F° equivale a %.1f C°";
            }
            else {
                outputTemperature = thermometer.convertCelsiusToFahrenheit(inputTemperature);
                outpuString = "A temperatura %.1f C° equivale a %.1f F°";
            }
            
            System.out.println(
                String.format(
                    outpuString, 
                    inputTemperature, 
                    outputTemperature
                )
            );
            System.out.println("Deseja continuar (s/n)?");
            String checkContinue = scanner.nextLine();
            isRunning = checkContinue.equals("s");
        }
        scanner.close();
    }
}
