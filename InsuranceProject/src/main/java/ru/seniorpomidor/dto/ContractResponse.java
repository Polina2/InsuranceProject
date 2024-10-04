package ru.seniorpomidor.dto;

import java.time.LocalDate;

public record ContractResponse(Long ID,
                               Long productID, LocalDate dateBegin, LocalDate dateEnd,
                               Long agentID, Double rate, Double commission, Long statusID,
                               Long policyHolderID, Long insuredPersonID, Long ownerID) {
}
