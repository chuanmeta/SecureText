package com.example.be.controllers;

import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class AppController {
    
    @GetMapping("/wellcome")
    public ResponseEntity wellcome() {
        Map<String, String> data = Map.of("title", "welcome");
        return ResponseEntity.ok(data);
    }
    
}
