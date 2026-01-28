if __name__ == "__main__":

    colors = ['red', 'green', 'blue']
    sizes = ['S', 'M', 'L']

    cartesian_product = [(color, size) for color in colors for size in sizes]
    
    print(cartesian_product)