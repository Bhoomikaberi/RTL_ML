module sequence_detector_fsm(
input clk,
input rst,
input x,
output reg y
);

reg [1:0] state;

always @(posedge clk or posedge rst)
begin

    if(rst)
    begin
        state <= 0;
        y <= 0;
    end

    else
    begin

        case(state)

        0:
            if(x)
                state <= 1;

        1:
            if(~x)
                state <= 2;

        2:
        begin
            if(x)
            begin
                y <= 1;
                state <= 0;
            end
        end

        endcase

    end

end

endmodule