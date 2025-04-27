# SQL Injection Demo Project

## Description
This project is a simple web application intentionally designed with SQL Injection vulnerabilities for educational purposes. It allows users to practice detecting and exploiting SQL injections using tools like **Burp Suite** and **Postman**.
It is ideal for cybersecurity learning, demonstrations, and awareness training.

> **Note**: This application is intentionally insecure and should **never** be deployed in a production environment.

---

## Features
- Insecure login/search forms vulnerable to SQL Injection.
- REST API endpoints easy to intercept and manipulate.
- Full Burp Suite and Postman testing compatibility.

---

## How to Perform SQL Injection

1. **Find a vulnerable field**:
   Typically, login forms, search bars, or any user input fields.

2. **Example SQL Injection Payloads**:
   - Login as admin without knowing the password (fill in the username only, leave password empty):
     ```
     admin' --
     ```
   - Login bypass (fill in the username only, leave password empty):
     ```
     ' OR '1'='1' --
     ```
   - Extract all users (for search fields):
     ```


3. **Observation**:
   If the app logs you in without valid credentials or leaks database errors/data, the SQL injection is successful.

---

## Configuring Burp Suite for Interception

1. Open **Burp Suite** and go to the **Proxy** tab.
2. Click **Options** -> Add a new proxy listener if necessary (default is 127.0.0.1:8080).
3. Go to **Proxy → Intercept** → Ensure **Intercept is ON**.
4. Configure your browser or Postman to use Burp Suite as a proxy:
   - **HTTP Proxy**: 127.0.0.1
   - **Port**: 8080
5. Install Burp’s **CA Certificate** if you want to intercept HTTPS traffic:
   - Visit http://burpsuite in the browser.
   - Download and install the certificate.

---

## Configuring Postman to Work with Burp Suite

1. Open **Postman**.
2. Go to **Settings → Proxy**.
3. Enable **Use System Proxy** or manually set:
   - Proxy Server: 127.0.0.1
   - Port: 8080
4. Send a request — it will now be captured by Burp Suite.
5. You can modify the requests in **Burp Suite** before forwarding them to the server.

---

## How to Configure and Run the Spring Boot Project in VSCode

1. **Install Prerequisites**:
   - Java Development Kit (JDK) 17 or higher.
   - Maven or Gradle (depending on your project setup).
   - Spring Boot Extension Pack in VSCode.

2. **Clone or Open the Project**:
   - Open VSCode.
   - Go to `File → Open Folder` and select the project directory.

3. **Configure the Database**:
   - Ensure PostgreSQL is running.
   - Update `application.properties` or `application.yml` with your database credentials.
     ```properties
     spring.datasource.url=jdbc:postgresql://localhost:5432/your_database_name
     spring.datasource.username=your_username
     spring.datasource.password=your_password
     ```

4. **Build the Project**:
   - Open the terminal in VSCode.
   - Run:
     ```bash
     ./mvnw clean install
     ```
     or if using Gradle:
     ```bash
     ./gradlew build
     ```

5. **Run the Application**:
   - Press `F5` or right-click on the main application class (`@SpringBootApplication`) and select **Run Java**.
   - Or from terminal:
     ```bash
     ./mvnw spring-boot:run
     ```

6. **Access the App**:
   - By default, the application will run on:
     ```
     http://localhost:8080
     ```

---

## Requirements
- Java 17 or higher
- Spring Boot
- PostgreSQL
- VSCode with Spring Boot extensions
- Burp Suite Community or Pro
- Postman

---

## Warning
This project is intended for **educational purposes only**.
Do **NOT** attack systems you do not have permission to test.
