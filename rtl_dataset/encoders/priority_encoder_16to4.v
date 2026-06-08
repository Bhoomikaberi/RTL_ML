module priority_encoder_16to4(
input [15:0] in,
output reg [3:0] out
);

always @(*)
begin

    casex(in)

        16'b1xxxxxxxxxxxxxxx : out = 4'd15;
        16'b01xxxxxxxxxxxxxx : out = 4'd14;
        16'b001xxxxxxxxxxxxx : out = 4'd13;
        16'b0001xxxxxxxxxxxx : out = 4'd12;
        16'b00001xxxxxxxxxxx : out = 4'd11;
        16'b000001xxxxxxxxxx : out = 4'd10;
        16'b0000001xxxxxxxxx : out = 4'd9;
        16'b00000001xxxxxxxx : out = 4'd8;
        default : out = 4'd0;

    endcase

end

endmodule