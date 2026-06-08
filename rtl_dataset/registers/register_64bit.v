module register_64bit(
input clk,
input [63:0] d,
output reg [63:0] q
);

always @(posedge clk)
begin
    q <= d;
end

endmodule