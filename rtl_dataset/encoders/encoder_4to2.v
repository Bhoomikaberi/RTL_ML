module encoder_4to2(
input [3:0] in,
output reg [1:0] out
);

always @(*) begin
case(in)
4'b0001: out=0;
4'b0010: out=1;
4'b0100: out=2;
4'b1000: out=3;
endcase
end

endmodule