package ru.seniorpomidor.dto;

import java.util.List;

public record ListContractsResponse(List<ContractResponse> contracts) {
}
