package Q3;

public class Vehicle {
    private String regNo;
    private String manufacturer;
    private String owner;
    private double CO2;
    private double CO;
    private double HC;
    private String pollutionStatus;

    public void checkPollutionStatus(){
        System.out.println("Checking in respective classes");
    }

    public Vehicle(String regNo, String manufacturer, String owner, double CO2, double CO, double HC, String pollutionStatus) {
        this.regNo = regNo;
        this.manufacturer = manufacturer;
        this.owner = owner;
        this.CO2 = CO2;
        this.CO = CO;
        this.HC = HC;
        this.pollutionStatus = pollutionStatus;
    }

    @Override
    public String toString() {
        return "Vehicle{" +
                "regNo='" + regNo + '\'' +
                ", manufacturer='" + manufacturer + '\'' +
                ", owner='" + owner + '\'' +
                ", CO2=" + CO2 +
                ", CO=" + CO +
                ", HC=" + HC +
                ", pollutionStatus='" + pollutionStatus + '\'' +
                '}';
    }

    public String getRegNo() {
        return regNo;
    }

    public void setRegNo(String regNo) {
        this.regNo = regNo;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public double getCO2() {
        return CO2;
    }

    public void setCO2(double CO2) {
        this.CO2 = CO2;
    }

    public double getCO() {
        return CO;
    }

    public void setCO(double CO) {
        this.CO = CO;
    }

    public double getHC() {
        return HC;
    }

    public void setHC(double HC) {
        this.HC = HC;
    }

    public String getPollutionStatus() {
        return pollutionStatus;
    }

    public void setPollutionStatus(String pollutionStatus) {
        this.pollutionStatus = pollutionStatus;
    }
}
