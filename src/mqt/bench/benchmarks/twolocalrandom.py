from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from qiskit.circuit.library import TwoLocal

if TYPE_CHECKING:  # pragma: no cover
    from qiskit import QuantumCircuit


def create_circuit(num_qubits: int) -> QuantumCircuit:
    """Returns a quantum circuit implementing the TwoLocal ansatz with random parameter
    values.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    """

    np.random.seed(10)
    qc = TwoLocal(num_qubits, "ry", "cx", entanglement="full", reps=3)
    num_params = qc.num_parameters
    qc = qc.assign_parameters(2 * np.pi * np.random.rand(num_params))
    qc.measure_all()
    qc.name = "twolocalrandom"

    return qc
