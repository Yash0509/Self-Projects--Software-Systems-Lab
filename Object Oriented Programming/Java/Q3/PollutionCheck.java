package Q3;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PollutionCheck {

    public static void main(String[] args) throws FileNotFoundException {

        FileInputStream fis=new FileInputStream("Q3\\vehicles.txt");
        Scanner sc=new Scanner(fis);
        List<Vehicle> vehicleList = new ArrayList<>();
        List<String> vehicleType = new ArrayList<>();

        while(sc.hasNextLine())
        {
            String s = sc.nextLine();
            String[] words=(s).split(",");
            Vehicle tmpVehicle = new Vehicle(words[0],words[1],words[2],20000.0,20000.0,20000.0,"UNSET");
            vehicleList.add(tmpVehicle);
            vehicleType.add(words[3]);
        }
        sc.close();

        FileInputStream fis2=new FileInputStream("Q3\\pollution.txt");
        Scanner sc2=new Scanner(fis2);

        while(sc2.hasNextLine())
        {
            String s = sc2.nextLine();
            String[] words=(s).split(",");
            String tmpVehicleregNo = words[0];
            double tmpVehicleCO2 = Double.parseDouble(words[1]);
            double tmpVehicleCO = Double.parseDouble(words[2]);
            double tmpVehicleHC = Double.parseDouble(words[3]);

            for(int i=0;i<vehicleList.size();i++){
                if(vehicleList.get(i).getRegNo().equals(tmpVehicleregNo)){
                    vehicleList.get(i).setCO2(tmpVehicleCO2);
                    vehicleList.get(i).setCO(tmpVehicleCO);
                    vehicleList.get(i).setHC(tmpVehicleHC);
                }
            }
        }

        FileInputStream fis3=new FileInputStream("Q3\\queries.txt");
        Scanner sc3=new Scanner(fis3);
        while(sc3.hasNextLine())
        {
            String s = sc3.nextLine();
            String[] words=(s).split(",");
            String tmpVehicleregNo = words[0];
            int flag=0;

            for(int i=0;i<vehicleList.size();i++){
                if(vehicleList.get(i).getRegNo().equals(tmpVehicleregNo)){
                    flag=1;
                    if(vehicleType.get(i).equals(" Car") || vehicleType.get(i).equals("Car")){
                        Car car = new Car(
                                vehicleList.get(i).getRegNo(),
                                vehicleList.get(i).getManufacturer(),
                                vehicleList.get(i).getOwner(),
                                vehicleList.get(i).getCO2(),
                                vehicleList.get(i).getCO(),
                                vehicleList.get(i).getHC(),
                                vehicleList.get(i).getPollutionStatus()
                        );
                        if(car.getHC()==20000.0 || car.getCO()==20000.0 || car.getCO2()==20000.0)
                            System.out.println("PENDING");
                        else {
                            car.checkPollutionStatus();
                            System.out.println(car.getPollutionStatus());
                        }
                    }
                    else if(vehicleType.get(i).equals(" Truck") || vehicleType.get(i).equals("Truck")){
                        Truck truck = new Truck(
                                vehicleList.get(i).getRegNo(),
                                vehicleList.get(i).getManufacturer(),
                                vehicleList.get(i).getOwner(),
                                vehicleList.get(i).getCO2(),
                                vehicleList.get(i).getCO(),
                                vehicleList.get(i).getHC(),
                                vehicleList.get(i).getPollutionStatus()
                        );
                        truck.checkPollutionStatus();
                        System.out.println(truck.getPollutionStatus());
                    }
                }
            }
            if(flag==0)
                System.out.println("NOT REGISTERED");
        }
    }
}