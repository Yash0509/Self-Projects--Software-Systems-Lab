package Q3;

public class Truck extends Vehicle{
    public Truck(String regNo, String manufacturer, String owner, double CO2, double CO, double HC, String pollutionStatus) {
        super(regNo, manufacturer, owner, CO2, CO, HC, pollutionStatus);
    }

    @Override
    public void checkPollutionStatus() {
        if(getCO2() <= 25 && getCO() <=0.8 && getHC() <= 1000)
            this.setPollutionStatus("PASS");
        else
            this.setPollutionStatus("FAIL");
    }

}
