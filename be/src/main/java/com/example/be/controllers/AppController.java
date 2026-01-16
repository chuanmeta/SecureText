package com.example.be.controllers;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import com.example.be.models.dtos.EncryptDTO;

import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;




@RestController
public class AppController {

    @Autowired
    RestTemplate rt;

    @Value("${python.service.url}")
    private String pythonServiceUrl;
    
    @GetMapping("/mkdir")
    public ResponseEntity<?> wellcome() {


        Object obj = rt.getForObject(pythonServiceUrl + "/mkdir", String.class);

        // return ResponseEntity.ok(Map.of("name", "springboot"));
        return ResponseEntity.ok(obj);
    }

    @GetMapping("/")
    public ResponseEntity<?> appInfo() {
        return ResponseEntity.ok(rt.getForObject(pythonServiceUrl + "/", String.class));
    }

    // Generate font
    @PostMapping("/gen-font")
    public ResponseEntity<?> createFont() {
        return ResponseEntity.ok(rt.getForObject(pythonServiceUrl + "/create-font", Map.class));
    }
    
    
    // Get Text Enpoint
    @PostMapping(value = "/get-text", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<?> getText(@ModelAttribute EncryptDTO dto) {

        Map<String, String> body = Map.of("fontName", dto.font,
            "text", dto.text
        );

        try {
            @SuppressWarnings("unchecked")
            Map<String, Object> map = rt.postForObject(pythonServiceUrl + "/encrypt",
                body,
                Map.class
            );
            return ResponseEntity.ok(map);
        } catch (Exception e){
            e.printStackTrace();
        }

        return ResponseEntity.ok(Map.of());
        
    }
    
}
