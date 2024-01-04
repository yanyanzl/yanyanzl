#!/usr/bin/env python3
# -*- coding: utf-8 -*-


## Event Formats

### <Button-1>
- A mouse button is pressed over the widget. Button 1 is the leftmost button, button 2 is the middle button (where available), and button 3 the rightmost button. When you press down a mouse button over a widget, Tkinter will automatically “grab” the mouse pointer, and subsequent mouse events (e.g. Motion and Release events) will then be sent to the current widget as long as the mouse button is held down, even if the mouse is moved outside the current widget. The current position of the mouse pointer (relative to the widget) is provided in the x and y members of the event object passed to the callback.

- You can use ButtonPress instead of Button, or even leave it out completely: <Button-1>, <ButtonPress-1>, and <1> are all synonyms. For clarity, I prefer the <Button-1> syntax.

### <B1-Motion>
- The mouse is moved, with mouse button 1 being held down (use B2 for the middle button, B3 for the right button). The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback.

### <ButtonRelease-1>
- Button 1 was released. The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback.

### <Double-Button-1>
- Button 1 was double clicked. You can use Double or Triple as prefixes. Note that if you bind to both a single click (<Button-1>) and a double click, both bindings will be called.

### <Enter>
# The mouse pointer entered the widget (this event doesn’t mean that the user pressed the Enter key!).

### <Leave>
- The mouse pointer left the widget.

### <FocusIn>
- Keyboard focus was moved to this widget, or to a child of this widget.

### <FocusOut>
- Keyboard focus was moved from this widget to another widget.

### <Return>
- The user pressed the Enter key. You can bind to virtually all keys on the keyboard. For an ordinary 102-key PC-style keyboard, the special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.

### <Key>
- The user pressed any key. The key is provided in the char member of the event object passed to the callback (this is an empty string for special keys).

### a
- The user typed an “a”. Most printable characters can be used as is. The exceptions are space (<space>) and less than (<less>). Note that 1 is a keyboard binding, while <1> is a button binding.

### <Shift-Up>
- The user pressed the Up arrow, while holding the Shift key pressed. You can use prefixes like Alt, Shift, and Control.

### <Configure>
The widget changed size (or location, on some platforms). The new size is provided in the width and height attributes of the event object passed to the callback.

## The Event Object

- The event object is a standard Python object instance, with a number of attributes describing the event.

## Event Attributes

### widget
The widget which generated this event. This is a valid Tkinter widget instance, not a name. This attribute is set for all events.

### x, y
- The current mouse position, in pixels.

### x_root, y_root
- The current mouse position relative to the upper left corner of the screen, in pixels.

### char
-The character code (keyboard events only), as a string.

### keysym
- The key symbol (keyboard events only).

### keycode
- The key code (keyboard events only).

### num
- The button number (mouse button events only).

### width, height
- The new size of the widget, in pixels (Configure events only).

### type
- The event type.

### For portability reasons, you should stick to char, height, width, x, y, x_root, y_root, and widget. Unless you know exactly what you’re doing, of course…

## Instance and Class Bindings

### The bind method we used in the above example creates an instance binding. This means that the binding applies to a single widget only; if you create new frames, they will not inherit the bindings.

### Tkinter also allows you to create bindings on the class and application level; in fact, you can create bindings on four different levels:

### the widget instance, using bind.

    - the widget’s toplevel window (Toplevel or root), also using bind.

### the widget class, using bind_class (this is used by Tkinter to provide standard bindings).

### the whole application, using bind_all.

    - For example, you can use bind_all to create a binding for the F1 key, so you can provide help everywhere in the application. But what happens if you create multiple bindings for the same key, or provide overlapping bindings?

    - First, on each of these four levels, Tkinter chooses the “closest match” of the available bindings. For example, if you create instance bindings for the <Key> and <Return> events, only the second binding will be called if you press the Enter key.

    - However, if you add a <Return> binding to the toplevel widget, both bindings will be called. Tkinter first calls the best binding on the instance level, then the best binding on the toplevel window level, then the best binding on the class level (which is often a standard binding), and finally the best available binding on the application level. So in an extreme case, a single event may call four event handlers.

### A common cause of confusion is when you try to use bindings to override the default behavior of a standard widget. For example, assume you wish to disable the Enter key in the text widget, so that the users cannot insert newlines into the text. Maybe the following will do the trick?
    ``` python
    def ignore(event):
        pass
    text.bind("<Return>", ignore)
    
    or, if you prefer one-liners:
    
    text.bind("<Return>", lambda e: None)
    ```









