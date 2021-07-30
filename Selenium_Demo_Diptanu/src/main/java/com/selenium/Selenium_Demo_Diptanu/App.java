package com.selenium.Selenium_Demo_Diptanu;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws InterruptedException, IOException
    {
        System.setProperty("webdriver.chrome.driver", "./driver/chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        
        String url = "https://twitter.com";
        driver.get(url);
        driver.manage().window().maximize();
        
        Thread.sleep(3000);
        
        WebElement login = driver.findElement(By.xpath("//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div"));
        login.click();
        Thread.sleep(3000);
        
        String username = "shayansaha85";
        String password = "7XvWx%w6XCWf@hYfFL*E&CiwvBFj3E&!G*69@dzJ";
        
        WebElement usernamebox, passwordbox;
        usernamebox = driver.findElement(By.name("session[username_or_email]"));
        passwordbox = driver.findElement(By.name("session[password]"));
        
        usernamebox.sendKeys(username);
        passwordbox.sendKeys(password);
        
        WebElement loginBtn = driver.findElement(By.xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div"));
        loginBtn.click();
        
        Thread.sleep(5000);
        takeScreenshot(driver, "screenshots/test.png");
        driver.quit();
        
        
        
    }
    
    public static void takeScreenshot(WebDriver driver, String path) throws IOException {
    	TakesScreenshot ss = (TakesScreenshot)driver;
    	File source = ss.getScreenshotAs(OutputType.FILE);
    	File destination = new File(path);
    	FileUtils.copyFile(source, destination);
    }
}
