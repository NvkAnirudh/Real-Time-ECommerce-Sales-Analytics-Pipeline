package Dto;
import java.util.Date;
import lombok.Data;
import lombok.AllArgsConstructor;

@Data
@AllArgsConstructor
public class SalesPerDay {
    private Date transactionDate;
    private double totalSales;

    public SalesPerDay(Date transactionDate, double totalSales) {
        this.transactionDate = transactionDate;
        this.totalSales = totalSales;
    }

    public Date getTransactionDate() {
        return transactionDate;
    }

    public double getTotalSales() {
        return totalSales;
    }

    public void setTotalSales(double totalSales) {
        this.totalSales = totalSales;
    }
}
