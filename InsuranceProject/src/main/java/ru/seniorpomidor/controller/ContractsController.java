package ru.seniorpomidor.controller;

import org.springframework.web.bind.annotation.*;
import ru.seniorpomidor.dto.*;

@RequestMapping("/contracts")
@RestController
public class ContractsController {
    @PostMapping("/new")
    public ContractResponse createContract(ContractRequest request) {
        return null;
    }

    @PatchMapping("/edit/{id}")
    public ContractResponse editContract(ContractRequest request) {
        return null;
    }

    @GetMapping
    public ListContractsResponse getContracts(@RequestHeader("agent-id") Long agentID) {
        return null;
    }

    @GetMapping("/premium")
    public PremiumResponse getPremium(PremiumRequest request) {
        return null;
    }
}
