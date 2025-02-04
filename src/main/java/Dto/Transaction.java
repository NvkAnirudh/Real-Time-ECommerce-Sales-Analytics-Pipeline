package Dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.sql.Timestamp;
import lombok.Data;

@Data
public class Transaction {
    @JsonProperty("transactionId")
    private String transactionId;

    @JsonProperty("productId")
    private String productId;

    @JsonProperty("productName")
    private String productName;

    @JsonProperty("productCategory")
    private String productCategory;

    @JsonProperty("productPrice")
    private double productPrice;

    @JsonProperty("productQuantity")
    private int productQuantity;

    @JsonProperty("productBrand")
    private String productBrand;

    @JsonProperty("totalAmount")
    private double totalAmount;

    @JsonProperty("currency")
    private String currency;

    @JsonProperty("customerId")
    private String customerId;

    @JsonProperty("transactionDate")
    private Timestamp transactionDate;

    @JsonProperty("paymentMethod")
    private String paymentMethod;

    // Getter methods
    public String getTransactionId() {
        return transactionId;
    }

    public String getProductId() {
        return productId;
    }

    public String getProductName() {
        return productName;
    }

    public String getProductCategory() {
        return productCategory;
    }

    public double getProductPrice() {
        return productPrice;
    }

    public int getProductQuantity() {
        return productQuantity;
    }

    public String getProductBrand() {
        return productBrand;
    }

    public double getTotalAmount() {
        return totalAmount;
    }

    public String getCurrency() {
        return currency;
    }

    public String getCustomerId() {
        return customerId;
    }

    public Timestamp getTransactionDate() {
        return transactionDate;
    }

    public String getPaymentMethod() {
        return paymentMethod;
    }
}


