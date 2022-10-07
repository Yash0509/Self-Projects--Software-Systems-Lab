package Q3;

public class Car extends Vehicle{

    public Car(String regNo, String manufacturer, String owner, double CO2, double CO, double HC, String pollutionStatus) {
        super(regNo, manufacturer, owner, CO2, CO, HC, pollutionStatus);
    }

    @Override
    public void checkPollutionStatus() {
        if(this.getCO2() <= 15 && this.getCO() <=0.5 && this.getHC() <= 750)
            this.setPollutionStatus("PASS");
        else
            this.setPollutionStatus("FAIL");
    }
}