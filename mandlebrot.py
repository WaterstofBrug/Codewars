import pyglet
import cmath
import math


def itteration(x, y, calc_depth):
    z = 0 + 0j
    c = complex(x, y)

    for i in range(calc_depth):
        z = z*z + c

    if math.sqrt(z.imag**2 + z.real**2) <= 2:
        return True
    else:
        return False


def orbits_lister(x, y, calc_depth, gen_multiplier):
    z = 0 + 0j
    c = complex(x, y)
    orbits_list = []

    for i in range(calc_depth):
        z = z*z + c
        orbits_list.append((z.real*gen_multiplier + gen_multiplier*2, z.imag*gen_multiplier + gen_multiplier*2))

    return orbits_list



def main():
    window_size = 1200
    win = pyglet.window.Window(window_size, window_size)
    batch = pyglet.graphics.Batch()

    calc_depth = 50
    pixel_size = 1
    generation_range = (-2, 2)
    generation_multiplier = int(window_size / generation_range[1] / 2)

    pixel_black = [[]]

    print('calculating')

    for y in range(generation_range[0] * generation_multiplier, generation_range[1] * generation_multiplier, pixel_size):
        pixel_black.append([])
        for x in range(generation_range[0] * generation_multiplier, generation_range[1] * generation_multiplier, pixel_size):
            try:
                pixel_black[-1].append(itteration(x / generation_multiplier, y / generation_multiplier, calc_depth))
            except OverflowError:
                pixel_black[-1].append(False)

    print('printing')
    pixels = []
    for posY, row in enumerate(pixel_black):
        x_start = 0
        x_end = 0
        state = False
        print(row)
        for posX, pixel in enumerate(row):
            if pixel == state:
                x_end += pixel_size
            else:
                if state:
                    pixels.append(pyglet.shapes.Rectangle(x_start, posY*pixel_size, x_end-x_start, pixel_size, (0, 0, 0), batch=batch))
                else:
                    pixels.append(pyglet.shapes.Rectangle(x_start, posY*pixel_size, x_end-x_start, pixel_size, (0, 0, 255),
                                                          batch=batch))
                x_start = x_end + 1
                x_end += 1
                state = pixel

        """
        if True not in row:
            pixels.append(pyglet.shapes.Rectangle(0, posY*pixel_size, window_size, pixel_size, (0, 0, 255), batch=batch))
        else:
            pixels.append([])
            for posX, pixel in enumerate(row):
                if pixel:
                    colour = (0, 0, 0)
                else:
                    colour = (0, 0, 255)
                pixels[posY].append(pyglet.shapes.Rectangle(posX*pixel_size, posY*pixel_size, pixel_size, pixel_size, colour, batch=batch))
        """

    orbit_depth = 50
    batch_orbits = pyglet.graphics.Batch()
    orbits = [pyglet.shapes.Circle(0, 0, 2, color=(240, 240, 240), batch=batch_orbits) for i in range(orbit_depth)]

    @win.event
    def on_mouse_motion(x, y, dx, dy):
        orbits_list = orbits_lister((x - window_size/2) / generation_multiplier, (y - window_size/2) / generation_multiplier, orbit_depth, generation_multiplier)

        for i, orbit in enumerate(orbits):
            orbit.x, orbit.y = orbits_list[i]


    @win.event
    def on_draw():
        win.clear()
        batch.draw()
        batch_orbits.draw()

    pyglet.app.run()


if __name__ == '__main__':
    main()
