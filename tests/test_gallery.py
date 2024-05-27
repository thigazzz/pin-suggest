from pinsuggest.gallery import Gallery

def test_change_the_number_of_images_to_get_of_a_album():
    gallery = Gallery()
    albuns = gallery.get_albuns() # TODO Fake requisition
    
    old_images = albuns[0].get_images()
    gallery.change_number_of_images(albuns[0], 5)
    new_images = albuns[0].get_images()

    assert len(new_images) != len(old_images)
    assert len(new_images) == 5