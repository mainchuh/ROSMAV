# autogenerated by genmsg_py from WifiNN.msg. Do not edit.
import roslib.message
import struct


class WifiNN(roslib.message.Message):
  _md5sum = "52868941085aea3ab1ea77d0d88e5d2d"
  _type = "batman_mesh_info/WifiNN"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string ip
uint32 quality

"""
  __slots__ = ['ip','quality']
  _slot_types = ['string','uint32']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   ip,quality
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(WifiNN, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ip is None:
        self.ip = ''
      if self.quality is None:
        self.quality = 0
    else:
      self.ip = ''
      self.quality = 0

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      length = len(self.ip)
      #serialize self.ip
      buff.write(struct.pack('<I%ss'%length, length, self.ip))
      buff.write(struct.pack('<I', self.quality))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      end = 0
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.ip
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.ip,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (self.quality,) = struct.unpack('<I',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      length = len(self.ip)
      #serialize self.ip
      buff.write(struct.pack('<I%ss'%length, length, self.ip))
      buff.write(struct.pack('<I', self.quality))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      end = 0
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.ip
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.ip,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (self.quality,) = struct.unpack('<I',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

