package com.example.be.controllers;

import java.util.Map;
import java.util.logging.Logger;

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

    @Value("${root.font.default}")
    private String rootFontDefault;
    

    // Generate font
    @PostMapping("/gen-font")
    public ResponseEntity<?> createFont(@RequestParam(name = "fontName", required = false) String fontName) {

        if(fontName == null) fontName = rootFontDefault;

        return ResponseEntity.ok(rt.getForObject(pythonServiceUrl + "/app/font/create-font/" + fontName , Map.class));
    }
    
    
    // Get Text Enpoint
    @PostMapping(value = "/get-text", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<?> getText(@ModelAttribute EncryptDTO dto) {

        try {
            Map<String, String> body = Map.of("fontName", dto.getFont(),
                "text", dto.getText()
            );

            @SuppressWarnings("unchecked")
            Map<String, Object> map = rt.postForObject(pythonServiceUrl + "app/font/encrypt",
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
