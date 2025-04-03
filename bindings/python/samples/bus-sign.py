#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class BusSign(SampleBase):
    def __init__(self, *args, **kwargs):
        super(BusSign, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 0, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text

        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)


        # time.sleep(0.05)
        # offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

   # /// <summary>
   #  /// Draws the text with the specified color.
   #  /// </summary>
   #  /// <param name="font">Font to draw text with.</param>
   #  /// <param name="x">The X coordinate of the starting point.</param>
   #  /// <param name="y">The Y coordinate of the starting point.</param>
   #  /// <param name="color">The color of the text.</param>
   #  /// <param name="text">Text to draw.</param>
   #  /// <param name="spacing">Additional spacing between characters.</param>
   #  /// <param name="vertical">Whether to draw the text vertically.</param>
   #  /// <returns>How many pixels was advanced on the screen.</returns>
   #  public int DrawText(RGBLedFont font, int x, int y, Color color, string text, int spacing = 0, bool vertical = false) =>
   #      font.DrawText(_canvas, x, y, color, text, spacing, vertical);

# Main function
if __name__ == "__main__":
    run_text = BusSign()
    if (not run_text.process()):
        run_text.print_help()
