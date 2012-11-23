# autogenerated by genmsg_py from availableNextHopsRequest.msg. Do not edit.
import roslib.message
import struct

import roslib.msg
import position_tracker.msg

class availableNextHopsRequest(roslib.message.Message):
  _md5sum = "245dda2f71151ee4142e9e843f08ab6a"
  _type = "path_generator/availableNextHopsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """position_tracker/Position cur_pos
position_tracker/Position[] neighbor_pos

================================================================================
MSG: position_tracker/Position
Header header
float64 x
float64 y
float64 theta

================================================================================
MSG: roslib/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['cur_pos','neighbor_pos']
  _slot_types = ['position_tracker/Position','position_tracker/Position[]']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   cur_pos,neighbor_pos
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(availableNextHopsRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.cur_pos is None:
        self.cur_pos = position_tracker.msg.Position()
      if self.neighbor_pos is None:
        self.neighbor_pos = []
    else:
      self.cur_pos = position_tracker.msg.Position()
      self.neighbor_pos = []

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<3I', self.cur_pos.header.seq, self.cur_pos.header.stamp.secs, self.cur_pos.header.stamp.nsecs))
      length = len(self.cur_pos.header.frame_id)
      #serialize self.cur_pos.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.cur_pos.header.frame_id))
      buff.write(struct.pack('<3d', self.cur_pos.x, self.cur_pos.y, self.cur_pos.theta))
      #serialize self.neighbor_pos
      length = len(self.neighbor_pos)
      buff.write(struct.pack('<I', length))
      for val1 in self.neighbor_pos:
        buff.write(struct.pack('<I', val1.header.seq))
        buff.write(struct.pack('<2I', val1.header.stamp.secs, val1.header.stamp.nsecs))
        length = len(val1.header.frame_id)
        #serialize val1.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.header.frame_id))
        buff.write(struct.pack('<3d', val1.x, val1.y, val1.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      if self.cur_pos is None:
        self.cur_pos = position_tracker.msg.Position()
      end = 0
      start = end
      end += 12
      (self.cur_pos.header.seq, self.cur_pos.header.stamp.secs, self.cur_pos.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.cur_pos.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.cur_pos.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 24
      (self.cur_pos.x, self.cur_pos.y, self.cur_pos.theta,) = struct.unpack('<3d',str[start:end])
      #deserialize self.neighbor_pos
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.neighbor_pos = []
      for i in xrange(0, length):
        val1 = position_tracker.msg.Position()
        start = end
        end += 4
        (val1.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.header.stamp.secs, val1.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.x, val1.y, val1.theta,) = struct.unpack('<3d',str[start:end])
        self.neighbor_pos.append(val1)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<3I', self.cur_pos.header.seq, self.cur_pos.header.stamp.secs, self.cur_pos.header.stamp.nsecs))
      length = len(self.cur_pos.header.frame_id)
      #serialize self.cur_pos.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.cur_pos.header.frame_id))
      buff.write(struct.pack('<3d', self.cur_pos.x, self.cur_pos.y, self.cur_pos.theta))
      #serialize self.neighbor_pos
      length = len(self.neighbor_pos)
      buff.write(struct.pack('<I', length))
      for val1 in self.neighbor_pos:
        buff.write(struct.pack('<I', val1.header.seq))
        buff.write(struct.pack('<2I', val1.header.stamp.secs, val1.header.stamp.nsecs))
        length = len(val1.header.frame_id)
        #serialize val1.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.header.frame_id))
        buff.write(struct.pack('<3d', val1.x, val1.y, val1.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      if self.cur_pos is None:
        self.cur_pos = position_tracker.msg.Position()
      end = 0
      start = end
      end += 12
      (self.cur_pos.header.seq, self.cur_pos.header.stamp.secs, self.cur_pos.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.cur_pos.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.cur_pos.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 24
      (self.cur_pos.x, self.cur_pos.y, self.cur_pos.theta,) = struct.unpack('<3d',str[start:end])
      #deserialize self.neighbor_pos
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.neighbor_pos = []
      for i in xrange(0, length):
        val1 = position_tracker.msg.Position()
        start = end
        end += 4
        (val1.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.header.stamp.secs, val1.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.x, val1.y, val1.theta,) = struct.unpack('<3d',str[start:end])
        self.neighbor_pos.append(val1)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

# autogenerated by genmsg_py from availableNextHopsResponse.msg. Do not edit.
import roslib.message
import struct

import roslib.msg
import position_tracker.msg

class availableNextHopsResponse(roslib.message.Message):
  _md5sum = "74db7b54a04777ce9534dc9a596e3b90"
  _type = "path_generator/availableNextHopsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """position_tracker/Position[] avail_next_hops


================================================================================
MSG: position_tracker/Position
Header header
float64 x
float64 y
float64 theta

================================================================================
MSG: roslib/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['avail_next_hops']
  _slot_types = ['position_tracker/Position[]']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   avail_next_hops
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(availableNextHopsResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.avail_next_hops is None:
        self.avail_next_hops = []
    else:
      self.avail_next_hops = []

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      #serialize self.avail_next_hops
      length = len(self.avail_next_hops)
      buff.write(struct.pack('<I', length))
      for val1 in self.avail_next_hops:
        buff.write(struct.pack('<I', val1.header.seq))
        buff.write(struct.pack('<2I', val1.header.stamp.secs, val1.header.stamp.nsecs))
        length = len(val1.header.frame_id)
        #serialize val1.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.header.frame_id))
        buff.write(struct.pack('<3d', val1.x, val1.y, val1.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      end = 0
      #deserialize self.avail_next_hops
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.avail_next_hops = []
      for i in xrange(0, length):
        val1 = position_tracker.msg.Position()
        start = end
        end += 4
        (val1.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.header.stamp.secs, val1.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.x, val1.y, val1.theta,) = struct.unpack('<3d',str[start:end])
        self.avail_next_hops.append(val1)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      #serialize self.avail_next_hops
      length = len(self.avail_next_hops)
      buff.write(struct.pack('<I', length))
      for val1 in self.avail_next_hops:
        buff.write(struct.pack('<I', val1.header.seq))
        buff.write(struct.pack('<2I', val1.header.stamp.secs, val1.header.stamp.nsecs))
        length = len(val1.header.frame_id)
        #serialize val1.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.header.frame_id))
        buff.write(struct.pack('<3d', val1.x, val1.y, val1.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      end = 0
      #deserialize self.avail_next_hops
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.avail_next_hops = []
      for i in xrange(0, length):
        val1 = position_tracker.msg.Position()
        start = end
        end += 4
        (val1.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.header.stamp.secs, val1.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.x, val1.y, val1.theta,) = struct.unpack('<3d',str[start:end])
        self.avail_next_hops.append(val1)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

class availableNextHops(roslib.message.ServiceDefinition):
  _type          = 'path_generator/availableNextHops'
  _md5sum = 'f5dedbcd134aa246c432cca1360aa1b2'
  _request_class  = availableNextHopsRequest
  _response_class = availableNextHopsResponse
