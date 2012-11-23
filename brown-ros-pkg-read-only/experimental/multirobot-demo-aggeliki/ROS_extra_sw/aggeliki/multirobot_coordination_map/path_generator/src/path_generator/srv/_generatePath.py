# autogenerated by genmsg_py from generatePathRequest.msg. Do not edit.
import roslib.message
import struct

import roslib.msg
import map_loader.msg
import position_tracker.msg

class generatePathRequest(roslib.message.Message):
  _md5sum = "8a066ee0722fff3ad3d331afe2a50ecf"
  _type = "path_generator/generatePathRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 type
map_loader/GraphMap gmap
position_tracker/Position init_pos
position_tracker/Position dst_pos

================================================================================
MSG: map_loader/GraphMap
Node[] nodes
Edge[] edges


================================================================================
MSG: map_loader/Node
int32 id
#Node previous
int32 distanceFromStart
position_tracker/Position p


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

================================================================================
MSG: map_loader/Edge
uint32 node1_id
uint32 node2_id
int32 distance


"""
  __slots__ = ['type','gmap','init_pos','dst_pos']
  _slot_types = ['uint32','map_loader/GraphMap','position_tracker/Position','position_tracker/Position']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   type,gmap,init_pos,dst_pos
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(generatePathRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.type is None:
        self.type = 0
      if self.gmap is None:
        self.gmap = map_loader.msg.GraphMap()
      if self.init_pos is None:
        self.init_pos = position_tracker.msg.Position()
      if self.dst_pos is None:
        self.dst_pos = position_tracker.msg.Position()
    else:
      self.type = 0
      self.gmap = map_loader.msg.GraphMap()
      self.init_pos = position_tracker.msg.Position()
      self.dst_pos = position_tracker.msg.Position()

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<I', self.type))
      #serialize self.gmap.nodes
      length = len(self.gmap.nodes)
      buff.write(struct.pack('<I', length))
      for val1 in self.gmap.nodes:
        buff.write(struct.pack('<2i', val1.id, val1.distanceFromStart))
        buff.write(struct.pack('<I', val1.p.header.seq))
        buff.write(struct.pack('<2I', val1.p.header.stamp.secs, val1.p.header.stamp.nsecs))
        length = len(val1.p.header.frame_id)
        #serialize val1.p.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.p.header.frame_id))
        buff.write(struct.pack('<3d', val1.p.x, val1.p.y, val1.p.theta))
      #serialize self.gmap.edges
      length = len(self.gmap.edges)
      buff.write(struct.pack('<I', length))
      for val1 in self.gmap.edges:
        buff.write(struct.pack('<2Ii', val1.node1_id, val1.node2_id, val1.distance))
      buff.write(struct.pack('<3I', self.init_pos.header.seq, self.init_pos.header.stamp.secs, self.init_pos.header.stamp.nsecs))
      length = len(self.init_pos.header.frame_id)
      #serialize self.init_pos.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.init_pos.header.frame_id))
      buff.write(struct.pack('<3d3I', self.init_pos.x, self.init_pos.y, self.init_pos.theta, self.dst_pos.header.seq, self.dst_pos.header.stamp.secs, self.dst_pos.header.stamp.nsecs))
      length = len(self.dst_pos.header.frame_id)
      #serialize self.dst_pos.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.dst_pos.header.frame_id))
      buff.write(struct.pack('<3d', self.dst_pos.x, self.dst_pos.y, self.dst_pos.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      if self.gmap is None:
        self.gmap = map_loader.msg.GraphMap()
      if self.init_pos is None:
        self.init_pos = position_tracker.msg.Position()
      if self.dst_pos is None:
        self.dst_pos = position_tracker.msg.Position()
      end = 0
      start = end
      end += 4
      (self.type,) = struct.unpack('<I',str[start:end])
      #deserialize self.gmap.nodes
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.gmap.nodes = []
      for i in xrange(0, length):
        val1 = map_loader.msg.Node()
        start = end
        end += 8
        (val1.id, val1.distanceFromStart,) = struct.unpack('<2i',str[start:end])
        start = end
        end += 4
        (val1.p.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.p.header.stamp.secs, val1.p.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.p.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.p.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.p.x, val1.p.y, val1.p.theta,) = struct.unpack('<3d',str[start:end])
        self.gmap.nodes.append(val1)
      #deserialize self.gmap.edges
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.gmap.edges = []
      for i in xrange(0, length):
        val1 = map_loader.msg.Edge()
        start = end
        end += 12
        (val1.node1_id, val1.node2_id, val1.distance,) = struct.unpack('<2Ii',str[start:end])
        self.gmap.edges.append(val1)
      start = end
      end += 12
      (self.init_pos.header.seq, self.init_pos.header.stamp.secs, self.init_pos.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.init_pos.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.init_pos.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 36
      (self.init_pos.x, self.init_pos.y, self.init_pos.theta, self.dst_pos.header.seq, self.dst_pos.header.stamp.secs, self.dst_pos.header.stamp.nsecs,) = struct.unpack('<3d3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.dst_pos.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.dst_pos.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 24
      (self.dst_pos.x, self.dst_pos.y, self.dst_pos.theta,) = struct.unpack('<3d',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<I', self.type))
      #serialize self.gmap.nodes
      length = len(self.gmap.nodes)
      buff.write(struct.pack('<I', length))
      for val1 in self.gmap.nodes:
        buff.write(struct.pack('<2i', val1.id, val1.distanceFromStart))
        buff.write(struct.pack('<I', val1.p.header.seq))
        buff.write(struct.pack('<2I', val1.p.header.stamp.secs, val1.p.header.stamp.nsecs))
        length = len(val1.p.header.frame_id)
        #serialize val1.p.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.p.header.frame_id))
        buff.write(struct.pack('<3d', val1.p.x, val1.p.y, val1.p.theta))
      #serialize self.gmap.edges
      length = len(self.gmap.edges)
      buff.write(struct.pack('<I', length))
      for val1 in self.gmap.edges:
        buff.write(struct.pack('<2Ii', val1.node1_id, val1.node2_id, val1.distance))
      buff.write(struct.pack('<3I', self.init_pos.header.seq, self.init_pos.header.stamp.secs, self.init_pos.header.stamp.nsecs))
      length = len(self.init_pos.header.frame_id)
      #serialize self.init_pos.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.init_pos.header.frame_id))
      buff.write(struct.pack('<3d3I', self.init_pos.x, self.init_pos.y, self.init_pos.theta, self.dst_pos.header.seq, self.dst_pos.header.stamp.secs, self.dst_pos.header.stamp.nsecs))
      length = len(self.dst_pos.header.frame_id)
      #serialize self.dst_pos.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.dst_pos.header.frame_id))
      buff.write(struct.pack('<3d', self.dst_pos.x, self.dst_pos.y, self.dst_pos.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      if self.gmap is None:
        self.gmap = map_loader.msg.GraphMap()
      if self.init_pos is None:
        self.init_pos = position_tracker.msg.Position()
      if self.dst_pos is None:
        self.dst_pos = position_tracker.msg.Position()
      end = 0
      start = end
      end += 4
      (self.type,) = struct.unpack('<I',str[start:end])
      #deserialize self.gmap.nodes
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.gmap.nodes = []
      for i in xrange(0, length):
        val1 = map_loader.msg.Node()
        start = end
        end += 8
        (val1.id, val1.distanceFromStart,) = struct.unpack('<2i',str[start:end])
        start = end
        end += 4
        (val1.p.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.p.header.stamp.secs, val1.p.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.p.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.p.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.p.x, val1.p.y, val1.p.theta,) = struct.unpack('<3d',str[start:end])
        self.gmap.nodes.append(val1)
      #deserialize self.gmap.edges
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.gmap.edges = []
      for i in xrange(0, length):
        val1 = map_loader.msg.Edge()
        start = end
        end += 12
        (val1.node1_id, val1.node2_id, val1.distance,) = struct.unpack('<2Ii',str[start:end])
        self.gmap.edges.append(val1)
      start = end
      end += 12
      (self.init_pos.header.seq, self.init_pos.header.stamp.secs, self.init_pos.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.init_pos.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.init_pos.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 36
      (self.init_pos.x, self.init_pos.y, self.init_pos.theta, self.dst_pos.header.seq, self.dst_pos.header.stamp.secs, self.dst_pos.header.stamp.nsecs,) = struct.unpack('<3d3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.dst_pos.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.dst_pos.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 24
      (self.dst_pos.x, self.dst_pos.y, self.dst_pos.theta,) = struct.unpack('<3d',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

# autogenerated by genmsg_py from generatePathResponse.msg. Do not edit.
import roslib.message
import struct

import path_navigator.msg
import roslib.msg
import map_loader.msg
import position_tracker.msg

class generatePathResponse(roslib.message.Message):
  _md5sum = "fd20651d4e00349491fe00ca51b68d1d"
  _type = "path_generator/generatePathResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """path_navigator/Waypoints w


================================================================================
MSG: path_navigator/Waypoints
map_loader/Node[] waypoints

================================================================================
MSG: map_loader/Node
int32 id
#Node previous
int32 distanceFromStart
position_tracker/Position p


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
  __slots__ = ['w']
  _slot_types = ['path_navigator/Waypoints']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   w
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(generatePathResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.w is None:
        self.w = path_navigator.msg.Waypoints()
    else:
      self.w = path_navigator.msg.Waypoints()

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      #serialize self.w.waypoints
      length = len(self.w.waypoints)
      buff.write(struct.pack('<I', length))
      for val1 in self.w.waypoints:
        buff.write(struct.pack('<2i', val1.id, val1.distanceFromStart))
        buff.write(struct.pack('<I', val1.p.header.seq))
        buff.write(struct.pack('<2I', val1.p.header.stamp.secs, val1.p.header.stamp.nsecs))
        length = len(val1.p.header.frame_id)
        #serialize val1.p.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.p.header.frame_id))
        buff.write(struct.pack('<3d', val1.p.x, val1.p.y, val1.p.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      if self.w is None:
        self.w = path_navigator.msg.Waypoints()
      end = 0
      #deserialize self.w.waypoints
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.w.waypoints = []
      for i in xrange(0, length):
        val1 = map_loader.msg.Node()
        start = end
        end += 8
        (val1.id, val1.distanceFromStart,) = struct.unpack('<2i',str[start:end])
        start = end
        end += 4
        (val1.p.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.p.header.stamp.secs, val1.p.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.p.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.p.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.p.x, val1.p.y, val1.p.theta,) = struct.unpack('<3d',str[start:end])
        self.w.waypoints.append(val1)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      #serialize self.w.waypoints
      length = len(self.w.waypoints)
      buff.write(struct.pack('<I', length))
      for val1 in self.w.waypoints:
        buff.write(struct.pack('<2i', val1.id, val1.distanceFromStart))
        buff.write(struct.pack('<I', val1.p.header.seq))
        buff.write(struct.pack('<2I', val1.p.header.stamp.secs, val1.p.header.stamp.nsecs))
        length = len(val1.p.header.frame_id)
        #serialize val1.p.header.frame_id
        buff.write(struct.pack('<I%ss'%length, length, val1.p.header.frame_id))
        buff.write(struct.pack('<3d', val1.p.x, val1.p.y, val1.p.theta))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      if self.w is None:
        self.w = path_navigator.msg.Waypoints()
      end = 0
      #deserialize self.w.waypoints
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.w.waypoints = []
      for i in xrange(0, length):
        val1 = map_loader.msg.Node()
        start = end
        end += 8
        (val1.id, val1.distanceFromStart,) = struct.unpack('<2i',str[start:end])
        start = end
        end += 4
        (val1.p.header.seq,) = struct.unpack('<I',str[start:end])
        start = end
        end += 8
        (val1.p.header.stamp.secs, val1.p.header.stamp.nsecs,) = struct.unpack('<2I',str[start:end])
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1.p.header.frame_id
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1.p.header.frame_id,) = struct.unpack(pattern, str[start:end])
        start = end
        end += 24
        (val1.p.x, val1.p.y, val1.p.theta,) = struct.unpack('<3d',str[start:end])
        self.w.waypoints.append(val1)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

class generatePath(roslib.message.ServiceDefinition):
  _type          = 'path_generator/generatePath'
  _md5sum = 'cc37f76a27ae92c1ea557e7fc74eda2b'
  _request_class  = generatePathRequest
  _response_class = generatePathResponse
