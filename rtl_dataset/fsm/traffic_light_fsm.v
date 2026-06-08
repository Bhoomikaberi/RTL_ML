module traffic_light_fsm(
input clk,
input rst,
output reg [1:0] state
);

parameter RED=0;
parameter YELLOW=1;
parameter GREEN=2;

always @(posedge clk or posedge rst)
begin
    if(rst)
        state <= RED;

    else
        case(state)

            RED: state <= GREEN;
            GREEN: state <= YELLOW;
            YELLOW: state <= RED;

        endcase
end

endmodule