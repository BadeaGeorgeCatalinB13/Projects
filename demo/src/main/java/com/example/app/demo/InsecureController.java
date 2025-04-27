package com.example.app.demo;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api") // You can change the base path if you want
public class InsecureController {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @PostMapping(value = "/login", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public Object login(@RequestBody LoginRequest loginRequest) {
        String sql = "SELECT * FROM users2 WHERE username = '" + loginRequest.getUsername() + 
                    "' AND password = '" + loginRequest.getPassword() + "'";

        try {
            List<User> users = jdbcTemplate.query(sql, (rs, rowNum) ->
                new User(
                    rs.getLong("id"),
                    rs.getString("username"),
                    rs.getString("password"),
                    rs.getString("role")
                ));

            if (!users.isEmpty()) {
                User user = users.get(0);
                if ("ADMIN".equals(user.getRole())) {
                    return getAllUsers();
                } else {
                    return Map.of("message", "Login successful!");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return Map.of("error", "Invalid credentials");
    }

    // Get all users (no protection, insecure on purpose)
    @GetMapping(value = "/users", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<User> getAllUsers() {
        String sql = "SELECT * FROM users2";

        return jdbcTemplate.query(sql, (rs, rowNum) ->
            new User(
                rs.getLong("id"),
                rs.getString("username"),
                rs.getString("password"),
                rs.getString("role")
            ));
    }
}
