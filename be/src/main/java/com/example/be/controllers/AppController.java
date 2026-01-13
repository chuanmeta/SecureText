package com.example.be.controllers;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;


@RestController
public class AppController {

    @Autowired
    RestTemplate rt;

    @Value("${python.service.url}")
    private String pythonServiceUrl;
    
    @GetMapping("/mkdir")
    public ResponseEntity<?> wellcome() {


        // Object obj = rt.getForObject(pythonServiceUrl + "/mkdir", String.class);

        return ResponseEntity.ok(Map.of("name", "springboot"));
    }
    
}
