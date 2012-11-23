# autogenerated by genmsg_py from topDownPos.msg. Do not edit.
import roslib.message
import struct

## \htmlinclude topDownPos.msg.html

class topDownPos(roslib.message.Message):
  _md5sum = "7f8be2666b5b18a1db5ae6e18b2a0607"
  _type = "irobot_test/topDownPos"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 posx
float32 posy
float32 yaw

"""
  __slots__ = ['posx','posy','yaw']
  _slot_types = ['float32','float32','float32']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   posx,posy,yaw
  ##
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    super(topDownPos, self).__init__(*args, **kwds)
    #message fields cannot be None, assign default values for those that are
    if self.posx is None:
      self.posx = 0.
    if self.posy is None:
      self.posy = 0.
    if self.yaw is None:
      self.yaw = 0.

  ## internal API method
  def _get_types(self): return topDownPos._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<3f', self.posx, self.posy, self.yaw))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      end = 0
      start = end
      end += 12
      (self.posx, self.posy, self.yaw,) = struct.unpack('<3f',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<3f', self.posx, self.posy, self.yaw))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      end = 0
      start = end
      end += 12
      (self.posx, self.posy, self.yaw,) = struct.unpack('<3f',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

