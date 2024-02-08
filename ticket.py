from datetime import date

class Ticket:
    def __init__(self, fare: int, expiry_date: date):
        self.__fare = fare
        self.__expiry_date = expiry_date

    @property
    def fare(self) -> int:
        return self.__fare

    @property
    def is_expired(self) -> bool:
        return date.today() > self.__expiry_date


class TicketGate:
    def __init__(self, min_fare: int):
        self.__min_fare = min_fare

    def is_passable(self, ticket: Ticket) -> bool:
        if ticket.is_expired:
            return False
        if ticket.fare < self.__min_fare:
            return False
        return True


class Passenger:
    def __init__(self, ticket: Ticket):
        self.__ticket = ticket
    
    # 改札の通過
    def pass_gate(self, gate: TicketGate):
        if gate.is_passable(self.__ticket):
            print("改札を通ったよ！")
            return
        print("改札を通れないよ...")


def main():
    ticket = Ticket(fare=250, expiry_date=date(2024, 2, 8))
    expired_ticket = Ticket(fare=250, expiry_date=date(2022, 2, 8))
    passenger = Passenger(ticket=ticket)
    gate = TicketGate(min_fare=180)

    # 自動改札を通過
    passenger.pass_gate(gate)

    bad_passanger = Passenger(ticket=expired_ticket)
    bad_passanger.pass_gate(gate)

if __name__ == '__main__':
    main()
