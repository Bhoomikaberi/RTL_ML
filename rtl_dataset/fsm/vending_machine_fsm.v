module vending_machine_fsm(
input clk,
input rst,
input coin,
output reg dispense
);

reg [1:0] state;

parameter S0 = 0;
parameter S1 = 1;
parameter S2 = 2;

always @(posedge clk or posedge rst)
begin

    if(rst)
    begin
        state <= S0;
        dispense <= 0;
    end

    else
    begin

        case(state)

        S0:
        begin
            dispense <= 0;
            if(coin)
                state <= S1;
        end

        S1:
        begin
            if(coin)
                state <= S2;
        end

        S2:
        begin
            dispense <= 1;
            state <= S0;
        end

        endcase

    end

end

endmodule