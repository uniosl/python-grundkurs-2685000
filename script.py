#!/usr/bin/env python3

from typing import List, Tuple

class BankAccount:
    """Eine Klasse zur Darstellung eines einfachen Bankkontos."""

    def __init__(self, inhaber: str, kontonummer: str, start_kontostand: float = 0.0):
        """Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand."""
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self._kontostand = start_kontostand
        self._transaktionen: List[Tuple[str, float]] = []

    def einzahlen(self, betrag: float) -> None:
        """Erhöht den Kontostand um den eingezahlten Betrag."""
        if betrag > 0:
            self._kontostand += betrag
            self._transaktionen.append(("Einzahlung", betrag))
            print(f"{betrag} EUR wurden eingezahlt.")
        else:
            raise ValueError("Einzahlung fehlgeschlagen: Betrag muss positiv sein.")

    def abheben(self, betrag: float) -> None:
        """Verringert den Kontostand um den abgehobenen Betrag, wenn genügend Guthaben vorhanden ist."""
        if betrag > 0:
            if self._kontostand >= betrag:
                self._kontostand -= betrag
                self._transaktionen.append(("Abhebung", betrag))
                print(f"{betrag} EUR wurden abgehoben.")
            else:
                raise ValueError("Abhebung fehlgeschlagen: Unzureichendes Guthaben.")
        else:
            raise ValueError("Abhebung fehlgeschlagen: Betrag muss positiv sein.")

    def get_kontostand(self) -> float:
        """Gibt den aktuellen Kontostand zurück."""
        return self._kontostand

    def get_transaktionen(self) -> List[Tuple[str, float]]:
        """Gibt eine Liste aller Transaktionen zurück."""
        return self._transaktionen

    def __str__(self) -> str:
        """Gibt eine benutzerfreundliche Darstellung des Kontos zurück."""
        return (
            f"Konto von {self.inhaber}\n"
            f"Kontonummer: {self.kontonummer}\n"
            f"Aktueller Kontostand: {self._kontostand:.2f} EUR"
        )
    
# Aufgabe: Erstellen Sie ein neues Jugendbankkonto, dass von der Klasse 
# BankAccount erbt und beschränken sie die Abhebungen auf maximal 25€.

class JugendBankAccount(BankAccount):
    """Eine Klasse zur Darstellung eines Jugendbankkontos mit Abhebungsbeschränkung."""
    def __init__(self, inhaber, kontonummer, start_kontostand = 0, abhebungslimit = 25):
        super().__init__(inhaber, kontonummer, start_kontostand)
        self._abhebungslimit = abhebungslimit

    def __str__(self) -> str:
        """Gibt eine benutzerfreundliche Darstellung des Jugendkontos zurück."""
        return (
            super().__str__() + f"\nAbhebungslimit: {self._abhebungslimit:.2f} EUR"
        )
    
    def setze_abhebungslimit(self, neues_limit: float) -> None:
        """Setzt ein neues Abhebungslimit."""
        if neues_limit > 0:
            self._abhebungslimit = neues_limit
        else:
            raise ValueError("Abhebungslimit muss positiv sein.")
        
    def get_abhebungslimit(self) -> float:
        """Gibt das aktuelle Abhebungslimit zurück."""
        return self._abhebungslimit

    def abheben(self, betrag: float) -> None:
        if betrag <= self._abhebungslimit:
            super().abheben(betrag)
        else:
            raise ValueError(f"Abhebung fehlgeschlagen: Maximalbetrag von {self._abhebungslimit} EUR überschritten.")

jugend_konto = JugendBankAccount("Max Mustermann Junior", "DE1234567890", 100, 25)
print(jugend_konto)

jugend_konto.einzahlen(100)
print(jugend_konto)

try:   
    jugend_konto.abheben(30)
except ValueError as e:
    print(e)

try:
    jugend_konto.abheben(20)
except ValueError as e:
    print(e)

print(jugend_konto.get_kontostand())
print(jugend_konto.get_abhebungslimit())
jugend_konto.setze_abhebungslimit(50)
print(jugend_konto.get_abhebungslimit())
