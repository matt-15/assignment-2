from order import Cart
import load_helper as dat_loader

class Address:
  def __init__(self, address, postal, country, city):
    self.address = address
    self.postal = postal
    self.country = country.capitalize()
    self.city = city

  def get_full_address(self):
    return self.address + " " + self.country + " " + self.postal


class User:
  def __init__(self, id, first_name, last_name, password, gender, contact, email):
    self.__id = id
    self.first_name = first_name
    self.email = email
    self.contact_number = contact
    self.last_name = last_name
    self.__password = password
    self.gender = gender
    self.is_authenticated = False

  def Change_password(self, new_pass):
    self.__password = new_pass

  def Check_password(self, password):
    if self.__password == password:
      return True
    else:
      return False

  def get_name(self):
    return self.first_name + ' ' + self.last_name

  def get_id(self):
    return self.__id


class Customer(User):
  def __init__(self, id, first_name, last_name, password, gender, email, address, contact):
    super().__init__(id, first_name, last_name, password, gender, contact, email)
    self.__address = address
    # Customer's cart creation
    cart_dat = dat_loader.load_data("Carts")
    cart_id = cart_dat["id"]
    cart_list = cart_dat["data"]
    c = Cart(cart_id, id, [])
    cart_list.append(c)
    dat_loader.write_data("Carts", cart_list)

  def set_address(self, address, postal, country, city):
    new_a = Address(address, postal, country, city)
    self.__address = new_a

  def get_address(self):
    return self.__address.get_full_address()

  def get_address_postal(self):
    return self.__address.postal

  def get_address_line(self):
    return self.__address.address

  def get_address_city(self):
    return self.__address.city

  def get_country(self):
    return self.__address.country


class Staff(User):
  def __init__(self, id, staff_id, first_name, last_name, password, gender, contact, email):
    super().__init__(id, first_name, last_name, password, gender, contact, email)
    self.__staff_id = staff_id
    self.customer_count = 0

  def get_staff_id(self):
    return self.__staff_id
