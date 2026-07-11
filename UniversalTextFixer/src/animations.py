# FUNCTIONS: 
# fade_in()

# Smoothly fades in a window 
def fade_in(window, alpha=0.0):
    alpha += 0.06

    if alpha >= 1.0:
        window.attributes("-alpha", 1.0)
        return
    
    window.attributes("-alpha",alpha)

    window.after(8,lambda: fade_in(window, alpha))

