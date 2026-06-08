module traffic_controller_fsm(
input clk,
input rst,
output reg [1:0] light
);

parameter RED=0;
parameter YELLOW=1;
parameter GREEN=2;

always @(posedge clk or posedge rst)
begin

    if(rst)
        light <= RED;

    else
    begin

        case(light)

        RED:
            light <= GREEN;

        GREEN:
            light <= YELLOW;

        YELLOW:
            light <= RED;

        endcase

    end

end

endmodule